import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00199, 0.003).lineTo(0.00199, 0.00348).lineTo(0.00151, 0.003).lineTo(0.00199, 0.00252).lineTo(0.00199, 0.003).close()
solid=wp_sketch0.add(loop0).extrude(0.0004956023679758781)
