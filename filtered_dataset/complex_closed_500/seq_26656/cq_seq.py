import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, -0.0).lineTo(0.00599, 0.0036).lineTo(0.00599, -0.00184).lineTo(0.0, -0.00184).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.015947692824783047)
