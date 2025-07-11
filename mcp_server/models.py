# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T13:22:50+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, RootModel, conint, constr


class AmazonResourceType(
    RootModel[constr(pattern=r'[\s\S]*', min_length=0, max_length=256)]
):
    root: constr(pattern=r'[\s\S]*', min_length=0, max_length=256)


class ComplianceStatus(RootModel[bool]):
    root: bool


class ConcurrentModificationException(RootModel[Any]):
    root: Any


class ConstraintViolationException(RootModel[Any]):
    root: Any


class DescribeReportCreationInput(BaseModel):
    pass


class ErrorCode(Enum):
    InternalServiceException = 'InternalServiceException'
    InvalidParameterException = 'InvalidParameterException'


class ErrorMessage(RootModel[str]):
    root: str


class ExcludeCompliantResources(RootModel[bool]):
    root: bool


class GroupByAttribute(Enum):
    TARGET_ID = 'TARGET_ID'
    REGION = 'REGION'
    RESOURCE_TYPE = 'RESOURCE_TYPE'


class IncludeComplianceDetails(RootModel[bool]):
    root: bool


class InternalServiceException(RootModel[Any]):
    root: Any


class InvalidParameterException(RootModel[Any]):
    root: Any


class LastUpdated(RootModel[str]):
    root: str


class MaxResultsGetComplianceSummary(RootModel[conint(ge=1, le=1000)]):
    root: conint(ge=1, le=1000)


class NonCompliantResources(RootModel[int]):
    root: int


class PaginationToken(
    RootModel[constr(pattern=r'[\s\S]*', min_length=0, max_length=2048)]
):
    root: constr(pattern=r'[\s\S]*', min_length=0, max_length=2048)


class PaginationTokenExpiredException(RootModel[Any]):
    root: Any


class Region(RootModel[constr(pattern=r'[\s\S]*', min_length=1, max_length=256)]):
    root: constr(pattern=r'[\s\S]*', min_length=1, max_length=256)


class RegionFilterList(RootModel[List[Region]]):
    root: List[Region] = Field(..., max_length=100, min_length=1)


class ResourceARN(RootModel[constr(pattern=r'[\s\S]*', min_length=1, max_length=1011)]):
    root: constr(pattern=r'[\s\S]*', min_length=1, max_length=1011)


class ResourceARNListForGet(RootModel[List[ResourceARN]]):
    root: List[ResourceARN] = Field(..., max_length=100, min_length=1)


class ResourceARNListForTagUntag(RootModel[List[ResourceARN]]):
    root: List[ResourceARN] = Field(..., max_length=20, min_length=1)


class ResourceTypeFilterList(RootModel[List[AmazonResourceType]]):
    root: List[AmazonResourceType]


class ResourcesPerPage(RootModel[int]):
    root: int


class S3Bucket(RootModel[constr(pattern=r'[a-z0-9.-]*', min_length=3, max_length=63)]):
    root: constr(pattern=r'[a-z0-9.-]*', min_length=3, max_length=63)


class S3Location(RootModel[str]):
    root: str


class StartReportCreationInput(BaseModel):
    S3Bucket_1: S3Bucket = Field(..., alias='S3Bucket')


class StartReportCreationOutput(BaseModel):
    pass


class Status(RootModel[str]):
    root: str


class StatusCode(RootModel[int]):
    root: int


class TagKey(RootModel[constr(pattern=r'[\s\S]*', min_length=1, max_length=128)]):
    root: constr(pattern=r'[\s\S]*', min_length=1, max_length=128)


class TagKeyFilterList(RootModel[List[TagKey]]):
    root: List[TagKey] = Field(..., max_length=50, min_length=1)


class TagKeyList(RootModel[List[TagKey]]):
    root: List[TagKey]


class TagKeyListForUntag(RootModel[List[TagKey]]):
    root: List[TagKey] = Field(..., max_length=50, min_length=1)


class TagValue(RootModel[constr(pattern=r'[\s\S]*', min_length=0, max_length=256)]):
    root: constr(pattern=r'[\s\S]*', min_length=0, max_length=256)


class TagValueList(RootModel[List[TagValue]]):
    root: List[TagValue] = Field(..., max_length=20, min_length=0)


class TagValuesOutputList(RootModel[List[TagValue]]):
    root: List[TagValue]


class TagsPerPage(RootModel[int]):
    root: int


class TargetId(
    RootModel[constr(pattern=r'[a-zA-Z0-9-]*', min_length=6, max_length=68)]
):
    root: constr(pattern=r'[a-zA-Z0-9-]*', min_length=6, max_length=68)


class TargetIdFilterList(RootModel[List[TargetId]]):
    root: List[TargetId] = Field(..., max_length=100, min_length=1)


class TargetIdType(Enum):
    ACCOUNT = 'ACCOUNT'
    OU = 'OU'
    ROOT = 'ROOT'


class ThrottledException(RootModel[Any]):
    root: Any


class UntagResourcesInput(BaseModel):
    ResourceARNList: ResourceARNListForTagUntag
    TagKeys: TagKeyListForUntag


class XAmzTarget(Enum):
    ResourceGroupsTaggingAPI_20170126_DescribeReportCreation = (
        'ResourceGroupsTaggingAPI_20170126.DescribeReportCreation'
    )


class XAmzTarget1(Enum):
    ResourceGroupsTaggingAPI_20170126_GetComplianceSummary = (
        'ResourceGroupsTaggingAPI_20170126.GetComplianceSummary'
    )


class XAmzTarget2(Enum):
    ResourceGroupsTaggingAPI_20170126_GetResources = (
        'ResourceGroupsTaggingAPI_20170126.GetResources'
    )


class XAmzTarget3(Enum):
    ResourceGroupsTaggingAPI_20170126_GetTagKeys = (
        'ResourceGroupsTaggingAPI_20170126.GetTagKeys'
    )


class XAmzTarget4(Enum):
    ResourceGroupsTaggingAPI_20170126_GetTagValues = (
        'ResourceGroupsTaggingAPI_20170126.GetTagValues'
    )


class XAmzTarget5(Enum):
    ResourceGroupsTaggingAPI_20170126_StartReportCreation = (
        'ResourceGroupsTaggingAPI_20170126.StartReportCreation'
    )


class XAmzTarget6(Enum):
    ResourceGroupsTaggingAPI_20170126_TagResources = (
        'ResourceGroupsTaggingAPI_20170126.TagResources'
    )


class XAmzTarget7(Enum):
    ResourceGroupsTaggingAPI_20170126_UntagResources = (
        'ResourceGroupsTaggingAPI_20170126.UntagResources'
    )


class ComplianceDetails(BaseModel):
    ComplianceStatus_1: Optional[ComplianceStatus] = Field(
        None, alias='ComplianceStatus'
    )
    KeysWithNoncompliantValues: Optional[TagKeyList] = None
    NoncompliantKeys: Optional[TagKeyList] = None


class DescribeReportCreationOutput(BaseModel):
    ErrorMessage_1: Optional[ErrorMessage] = Field(None, alias='ErrorMessage')
    S3Location_1: Optional[S3Location] = Field(None, alias='S3Location')
    Status_1: Optional[Status] = Field(None, alias='Status')


class FailureInfo(BaseModel):
    ErrorCode_1: Optional[ErrorCode] = Field(None, alias='ErrorCode')
    ErrorMessage_1: Optional[ErrorMessage] = Field(None, alias='ErrorMessage')
    StatusCode_1: Optional[StatusCode] = Field(None, alias='StatusCode')


class GetTagKeysInput(BaseModel):
    PaginationToken_1: Optional[PaginationToken] = Field(None, alias='PaginationToken')


class GetTagKeysOutput(BaseModel):
    PaginationToken_1: Optional[PaginationToken] = Field(None, alias='PaginationToken')
    TagKeys: Optional[TagKeyList] = None


class GetTagValuesInput(BaseModel):
    Key: TagKey
    PaginationToken_1: Optional[PaginationToken] = Field(None, alias='PaginationToken')


class GetTagValuesOutput(BaseModel):
    PaginationToken_1: Optional[PaginationToken] = Field(None, alias='PaginationToken')
    TagValues: Optional[TagValuesOutputList] = None


class GroupBy(RootModel[List[GroupByAttribute]]):
    root: List[GroupByAttribute]


class Summary(BaseModel):
    LastUpdated_1: Optional[LastUpdated] = Field(None, alias='LastUpdated')
    NonCompliantResources_1: Optional[NonCompliantResources] = Field(
        None, alias='NonCompliantResources'
    )
    Region_1: Optional[Region] = Field(None, alias='Region')
    ResourceType: Optional[AmazonResourceType] = None
    TargetId_1: Optional[TargetId] = Field(None, alias='TargetId')
    TargetIdType_1: Optional[TargetIdType] = Field(None, alias='TargetIdType')


class SummaryList(RootModel[List[Summary]]):
    root: List[Summary]


class Tag(BaseModel):
    Key: TagKey
    Value: TagValue


class TagFilter(BaseModel):
    Key: Optional[TagKey] = None
    Values: Optional[TagValueList] = None


class TagFilterList(RootModel[List[TagFilter]]):
    root: List[TagFilter] = Field(..., max_length=50, min_length=0)


class TagList(RootModel[List[Tag]]):
    root: List[Tag]


class TagMap(RootModel[Optional[Dict[str, TagValue]]]):
    root: Optional[Dict[str, TagValue]] = None


class TagResourcesInput(BaseModel):
    ResourceARNList: ResourceARNListForTagUntag
    Tags: TagMap


class FailedResourcesMap(RootModel[Optional[Dict[str, FailureInfo]]]):
    root: Optional[Dict[str, FailureInfo]] = None


class GetComplianceSummaryInput(BaseModel):
    GroupBy_1: Optional[GroupBy] = Field(None, alias='GroupBy')
    MaxResults: Optional[MaxResultsGetComplianceSummary] = None
    PaginationToken_1: Optional[PaginationToken] = Field(None, alias='PaginationToken')
    RegionFilters: Optional[RegionFilterList] = None
    ResourceTypeFilters: Optional[ResourceTypeFilterList] = None
    TagKeyFilters: Optional[TagKeyFilterList] = None
    TargetIdFilters: Optional[TargetIdFilterList] = None


class GetComplianceSummaryOutput(BaseModel):
    PaginationToken_1: Optional[PaginationToken] = Field(None, alias='PaginationToken')
    SummaryList_1: Optional[SummaryList] = Field(None, alias='SummaryList')


class GetResourcesInput(BaseModel):
    ExcludeCompliantResources_1: Optional[ExcludeCompliantResources] = Field(
        None, alias='ExcludeCompliantResources'
    )
    IncludeComplianceDetails_1: Optional[IncludeComplianceDetails] = Field(
        None, alias='IncludeComplianceDetails'
    )
    PaginationToken_1: Optional[PaginationToken] = Field(None, alias='PaginationToken')
    ResourceARNList: Optional[ResourceARNListForGet] = None
    ResourceTypeFilters: Optional[ResourceTypeFilterList] = None
    ResourcesPerPage_1: Optional[ResourcesPerPage] = Field(
        None, alias='ResourcesPerPage'
    )
    TagFilters: Optional[TagFilterList] = None
    TagsPerPage_1: Optional[TagsPerPage] = Field(None, alias='TagsPerPage')


class ResourceTagMapping(BaseModel):
    ComplianceDetails_1: Optional[ComplianceDetails] = Field(
        None, alias='ComplianceDetails'
    )
    ResourceARN_1: Optional[ResourceARN] = Field(None, alias='ResourceARN')
    Tags: Optional[TagList] = None


class ResourceTagMappingList(RootModel[List[ResourceTagMapping]]):
    root: List[ResourceTagMapping]


class TagResourcesOutput(BaseModel):
    FailedResourcesMap_1: Optional[FailedResourcesMap] = Field(
        None, alias='FailedResourcesMap'
    )


class UntagResourcesOutput(BaseModel):
    FailedResourcesMap_1: Optional[FailedResourcesMap] = Field(
        None, alias='FailedResourcesMap'
    )


class GetResourcesOutput(BaseModel):
    PaginationToken_1: Optional[PaginationToken] = Field(None, alias='PaginationToken')
    ResourceTagMappingList_1: Optional[ResourceTagMappingList] = Field(
        None, alias='ResourceTagMappingList'
    )
