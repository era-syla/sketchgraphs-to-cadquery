import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.015, 0.051).lineTo(0.015, 0.051).lineTo(0.015, -0.023).lineTo(-0.015, -0.023).lineTo(-0.015, 0.051).close()
solid=wp_sketch0.add(loop0).extrude(0.20288681397849465)
