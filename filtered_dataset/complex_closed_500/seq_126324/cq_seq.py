import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00225, 0.00275).lineTo(0.00275, 0.00275).lineTo(0.00275, -0.00225).lineTo(0.002, -0.00225).lineTo(0.002, 0.002).lineTo(-0.00225, 0.002).lineTo(-0.00225, 0.00275).close()
solid=wp_sketch0.add(loop0).extrude(0.01149980945519598)
