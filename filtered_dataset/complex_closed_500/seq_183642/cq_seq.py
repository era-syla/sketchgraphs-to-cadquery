import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.05824, -0.05602).lineTo(-0.0232, -0.05602).lineTo(-0.0232, 0.04971).lineTo(-0.05824, 0.04971).lineTo(-0.05824, -0.05602).close()
solid=wp_sketch0.add(loop0).extrude(0.10925178036883362)
