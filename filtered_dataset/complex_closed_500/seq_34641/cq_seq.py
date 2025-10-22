import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.07545, 0.06583).lineTo(0.04455, 0.06583).lineTo(0.04455, 0.00883).lineTo(-0.07545, 0.00883).lineTo(-0.07545, 0.06583).close()
solid=wp_sketch0.add(loop0).extrude(-0.13352858316262764)
