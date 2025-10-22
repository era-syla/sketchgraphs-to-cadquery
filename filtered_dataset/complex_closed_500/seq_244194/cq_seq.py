import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0606, 0.005).lineTo(-0.0216, 0.005).lineTo(-0.0216, 0.0049).lineTo(-0.0606, 0.0049).lineTo(-0.0606, 0.005).close()
solid=wp_sketch0.add(loop0).extrude(-0.057211430169581586)
