import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.00724).lineTo(0.01548, 0.00724).lineTo(0.01548, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.00724).close()
solid=wp_sketch0.add(loop0).extrude(-0.008959388631114706)
