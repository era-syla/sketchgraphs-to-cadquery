import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00737, 0.04178).lineTo(0.01737, 0.04178).lineTo(0.01737, 0.03178).lineTo(0.00737, 0.03178).lineTo(0.00737, 0.04178).close()
solid=wp_sketch0.add(loop0).extrude(0.012285842053545767)
