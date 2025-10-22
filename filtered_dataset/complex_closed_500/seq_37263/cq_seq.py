import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.01739, 0.03463).lineTo(-0.01738, 0.03463).lineTo(-0.01738, 0.03464).lineTo(-0.01739, 0.03464).lineTo(-0.01739, 0.03463).close()
solid=wp_sketch0.add(loop0).extrude(-1.3841856450318622e-05)
