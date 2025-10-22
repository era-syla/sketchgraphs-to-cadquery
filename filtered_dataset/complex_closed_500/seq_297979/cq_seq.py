import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0508).lineTo(0.00254, 0.0508).lineTo(0.00254, 0.00254).lineTo(0.0508, 0.00254).lineTo(0.0508, 0.0).lineTo(0.0, 0.0).lineTo(-0.0, 0.0508).close()
solid=wp_sketch0.add(loop0).extrude(-0.04874861601221291)
