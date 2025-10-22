import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.24, -0.2695).lineTo(-0.25, -0.2695).lineTo(-0.25, -0.2655).lineTo(-0.24, -0.2655).lineTo(-0.24, -0.2695).close()
solid=wp_sketch0.add(loop0).extrude(0.013146683839528725)
