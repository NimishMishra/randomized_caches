#ifndef __ENUM__StaticInstFlags__Flags__
#define __ENUM__StaticInstFlags__Flags__

struct StaticInstFlags {
    enum Flags {
        IsNop = 0,
        IsInteger = 1,
        IsFloating = 2,
        IsCC = 3,
        IsVector = 4,
        IsVectorElem = 5,
        IsMemRef = 6,
        IsLoad = 7,
        IsStore = 8,
        IsAtomic = 9,
        IsStoreConditional = 10,
        IsIndexed = 11,
        IsInstPrefetch = 12,
        IsDataPrefetch = 13,
        IsControl = 14,
        IsDirectControl = 15,
        IsIndirectControl = 16,
        IsCondControl = 17,
        IsUncondControl = 18,
        IsCall = 19,
        IsReturn = 20,
        IsCondDelaySlot = 21,
        IsThreadSync = 22,
        IsSerializing = 23,
        IsSerializeBefore = 24,
        IsSerializeAfter = 25,
        IsMemBarrier = 26,
        IsWriteBarrier = 27,
        IsReadBarrier = 28,
        IsERET = 29,
        IsNonSpeculative = 30,
        IsQuiesce = 31,
        IsIprAccess = 32,
        IsUnverifiable = 33,
        IsSyscall = 34,
        IsMacroop = 35,
        IsMicroop = 36,
        IsDelayedCommit = 37,
        IsLastMicroop = 38,
        IsFirstMicroop = 39,
        IsMicroBranch = 40,
        IsDspOp = 41,
        IsSquashAfter = 42,
        Num_Flags = 43
    };
    static const char *FlagsStrings[Num_Flags];
};

#endif // __ENUM__StaticInstFlags__Flags__
