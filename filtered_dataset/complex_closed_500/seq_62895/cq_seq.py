import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.32385, 0.41593).lineTo(0.66675, 0.41593).lineTo(0.66675, 0.02857).lineTo(0.32385, 0.02857).lineTo(0.32385, 0.41593).close()
solid=wp_sketch0.add(loop0).extrude(-0.5530024838839345)
