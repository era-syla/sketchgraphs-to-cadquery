import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.14681, 0.00559).lineTo(0.00559, 0.00559).lineTo(0.00559, 0.13259).lineTo(0.14681, 0.13259).lineTo(0.14681, 0.00559).close()
solid=wp_sketch0.add(loop0).extrude(-0.1214819032871819)
