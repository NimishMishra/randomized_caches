
#echo "L2 accesses"
#find . -type f -exec grep -H "system.l2.tags.data_accesses" {} +

echo ""
echo "L2 misses"
find . -type f -exec grep -H "system.l2.overall_misses::.cpu1.data" {} +

#echo ""
#echo "L2 hits"
#find . -type f -exec grep -H "system.l2.overall_hits::.cpu1.data" {} +
