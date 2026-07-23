# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
# Compatibility shim: vllm-ascend references SharedFusedMoE which does not
# yet exist in upstream vllm. This provides a minimal base class so that
# vendor plugins (e.g. vllm-ascend-hust) can extend it via multiple
# inheritance. The real shared-expert logic lives in the vendor plugin.


class SharedFusedMoE:
    """Base class for FusedMoE with shared-expert overlap support.

    Vendor plugins override forward_impl to integrate shared expert
    computation with the MoE dispatch/combine pipeline.
    """

    pass
