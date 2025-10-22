import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.075, -0.12).lineTo(-0.075, -0.12).lineTo(-0.075, 0.12).lineTo(0.075, 0.12).lineTo(0.075, -0.12).close()
solid=wp_sketch0.add(loop0).extrude(0.49017879302686207)
