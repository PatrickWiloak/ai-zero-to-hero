# Section 5: Performance Optimization (10%)

**Last reviewed:** 2026-11-07

Four objectives on [NVIDIA's exam page](https://www.nvidia.com/en-us/learn/certification/generative-ai-multimodal-associate/) (checked 2026-11-07): enhance computational efficiency and output accuracy; optimize model performance including hyperparameter tuning; develop content on multimodal-specific transfer learning; and assist with model training and training optimization under supervision. The reading list names mixed precision training, quantization, pruning, NVIDIA Triton and NVIDIA NeMo. Code ran on CPU (PyTorch 2.15.0+cpu); GPU-specific effects (speed-ups from tensor cores) were not measured.

## Mixed precision

Mixed precision runs most operations in a lower-precision type to save memory and time, keeping sensitive operations in float32. PyTorch's `torch.autocast` does this: per the docs "some operations use the torch.float32 datatype and other operations use lower precision floating point datatype". Autocast wraps only the forward pass and loss computation, not `backward()`. For float16, you also need `GradScaler`, which multiplies the loss by a scale factor so small gradients do not underflow to zero, then unscales before the optimizer step; bfloat16 has float32's range and needs only autocast. On CPU the autocast dtype is bfloat16, with ops such as linear, conv and matmul in bfloat16 and many loss ops kept in float32.

**[📖 torch.amp: automatic mixed precision](https://docs.pytorch.org/docs/2.15/amp.html)** - autocast, GradScaler and CPU behavior

I checked the dtypes:

```python
with torch.autocast(device_type="cpu", dtype=torch.bfloat16):
    y = lin(x); z = F.mse_loss(y, x)
```

```
autocast bf16: linear output dtype torch.bfloat16 | loss dtype torch.float32 | weights dtype torch.float32
```

The linear layer's output is bfloat16, the loss is computed in float32, and the stored weights remain float32. That split is the whole idea: low-precision compute, full-precision master weights.

- **Mixed precision** - training with lower-precision arithmetic for most operations while keeping weights and sensitive operations in float32.
- **GradScaler** - the PyTorch helper that scales the loss for float16 training so small gradients do not underflow.

## Quantization

Quantization stores weights (and sometimes activations) in fewer bits, such as int8, to shrink the model and speed inference. Dynamic quantization converts weights ahead of time and activations at run time. I applied it to a two-layer model:

```python
qm = torch.ao.quantization.quantize_dynamic(mq, {nn.Linear}, dtype=torch.qint8)
```

```
dynamic quantization: fp32 2103517 bytes -> int8 531981 bytes (4.0x smaller)
```

Four times smaller, as expected for 32-bit to 8-bit weights. A maintenance note from the PyTorch 2.15 documentation: "We are centralizing all quantization related development to torchao" and "We plan to delete `torch.ao.quantization` in 2.10 if there are no blockers" (the call above still ran in 2.15 in my environment). Eager-mode users are directed to torchao's `quantize_` API. For the exam, know the concept and the size/speed trade-off against some accuracy loss; for new code, check torchao.

**[📖 PyTorch quantization](https://docs.pytorch.org/docs/2.15/quantization.html)** - The migration notice to torchao

- **Quantization** - representing weights (and possibly activations) with fewer bits, such as int8, to cut memory and speed up inference at a possible cost in accuracy.

## Pruning

Pruning zeros out weights judged unimportant. PyTorch's `torch.nn.utils.prune` offers `l1_unstructured` (zero the smallest-magnitude entries) and `global_unstructured` (prune across the whole model at once). The tutorial explains that pruning replaces the `weight` parameter with `weight_orig` plus a `weight_mask` buffer, recomputing the pruned weight in a forward pre-hook, and that `prune.remove` makes it permanent. I reproduced it:

```
pruning: params now ['bias', 'weight_orig'] | buffers ['weight_mask'] | sparsity 50.0%
after prune.remove params: ['bias', 'weight']
```

**[📖 Pruning tutorial](https://docs.pytorch.org/tutorials/intermediate/pruning_tutorial.html)** - l1_unstructured, global_unstructured, weight_orig and weight_mask

Unstructured pruning leaves zeros scattered through dense tensors, so it saves memory only with sparse storage or hardware support; do not assume a 50 percent sparse dense matrix runs twice as fast. That caveat is general knowledge rather than a quote from the tutorial.

- **Pruning** - removing (zeroing) weights that contribute little, to reduce model size or computation.

## Hyperparameter tuning and training optimization

Tuning searches settings such as learning rate, batch size and depth. Grid, random and Bayesian strategies are explained in the [Databricks ML Associate model development note](../../../databricks/ml-associate/notes/03-model-development.md) with a run of Hyperopt; the same ideas apply here. Training optimization covers the efficiency tools above, plus gradient clipping (note 1) and early stopping. The reading list includes NVIDIA NeMo, described in its docs as "a scalable and cloud-native generative AI framework" built on PyTorch, with documented support for mixed precision and model optimization (quantization, pruning, distillation) among other topics; the pages I read do not detail them.

**[📖 NVIDIA NeMo Framework overview](https://docs.nvidia.com/nemo-framework/user-guide/latest/overview.html)** - What NeMo is and which training topics it documents

## Multimodal-specific transfer learning

Covered in note 1 (freeze the pretrained encoders, train projection or fusion layers: 1.9 percent of parameters in my toy example). In an optimization context it is also the cheapest way to improve accuracy per unit of compute.

## Triton for serving efficiency

NVIDIA Triton Inference Server serves models from frameworks such as TensorRT, PyTorch, ONNX, OpenVINO, Python and RAPIDS FIL. Its per-model scheduler can group incoming requests into batches (dynamic batching), several models can run concurrently, models live in a file-system model repository, clients use HTTP/REST or gRPC (KServe protocol), and metrics expose GPU utilization, throughput and latency.

**[📖 Triton Inference Server user guide](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)** - Backends, dynamic batching, model repository and metrics

- **Dynamic batching** - a Triton scheduler feature that groups incoming requests into batches to raise throughput.

## Check yourself against the objectives

Say what autocast keeps in float32 and why GradScaler exists; compute the size effect of int8; explain `weight_orig` and `weight_mask`; and name two ways Triton raises serving efficiency. Questions are in the [NCA-GENM practice bank](../../../practice-questions/nvidia-generative-ai-multimodal-associate.md).
