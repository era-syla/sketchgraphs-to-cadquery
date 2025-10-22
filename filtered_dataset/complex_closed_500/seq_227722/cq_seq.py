import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.00318).lineTo(0.0127, 0.00318).lineTo(0.0127, 0.0).lineTo(-0.00254, -0.0).lineTo(-0.00254, 0.00673).lineTo(-0.30226, 0.00673).lineTo(-0.30226, 0.00317).lineTo(-0.3048, 0.00317).lineTo(-0.3048, 0.00927).lineTo(0.0, 0.00927).lineTo(0.0, 0.00318).close()
solid=wp_sketch0.add(loop0).extrude(-0.40735887587463127)
