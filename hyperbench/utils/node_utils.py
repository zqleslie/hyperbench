from torch import Tensor
from typing import Literal, TypeAlias
from collections.abc import Sequence


NodeSpaceAssignment: TypeAlias = Literal["first", "all"]
NodeSpaceFiller: TypeAlias = float | int | Sequence[float] | Tensor
NodeSpaceSetting: TypeAlias = Literal["inductive", "transductive"]


def assign_hyperedge_label_to_nodes(
    hyperedge_index: Tensor,
    y: Tensor,
    num_hyperedges: int,
) -> dict[frozenset[int], float]:
    labels_by_nodes = {}
    for hyperedge_id in range(num_hyperedges):
        mask = hyperedge_index[1] == hyperedge_id
        nodes = frozenset(hyperedge_index[0][mask].tolist())
        labels_by_nodes[nodes] = y[hyperedge_id]
    return labels_by_nodes


def is_assigned_to_all(node_space_assignment: NodeSpaceAssignment | None) -> bool:
    return node_space_assignment == "all"


def is_assigned_to_first(node_space_assignment: NodeSpaceAssignment | None) -> bool:
    return node_space_assignment == "first"


def is_inductive_setting(node_space_setting: NodeSpaceSetting | None) -> bool:
    return node_space_setting == "inductive"


def is_transductive_setting(node_space_setting: NodeSpaceSetting | None) -> bool:
    return node_space_setting == "transductive"


def is_transductive_split(
    node_space_setting: NodeSpaceSetting | None,
    assign_node_space_to: NodeSpaceAssignment | None,
    split_num: int,
) -> bool:
    if not is_transductive_setting(node_space_setting):
        return False
    if is_assigned_to_all(assign_node_space_to):
        return True
    return is_assigned_to_first(assign_node_space_to) and split_num == 0
