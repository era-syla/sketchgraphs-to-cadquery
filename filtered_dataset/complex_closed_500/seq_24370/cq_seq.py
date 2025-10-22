import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.2, 0.27543).lineTo(-0.2, 0.27543).lineTo(-0.2, -0.27543).lineTo(0.2, -0.27543).lineTo(0.2, 0.27543).close()
solid=wp_sketch0.add(loop0).extrude(0.10125172816366042)
