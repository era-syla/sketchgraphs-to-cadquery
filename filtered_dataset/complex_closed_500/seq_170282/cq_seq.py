import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03833, 0.03937).lineTo(0.05587, 0.03937).lineTo(0.08267, 0.03937).lineTo(0.08267, -0.08163).lineTo(-0.03833, -0.08163).lineTo(-0.03833, 0.03937).close()
solid=wp_sketch0.add(loop0).extrude(-0.2781544590995448)
