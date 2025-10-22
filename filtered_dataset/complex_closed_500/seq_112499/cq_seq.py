import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.00392, -0.01).lineTo(0.00392, 0.0).lineTo(0.01392, 0.0).lineTo(0.01392, -0.002).lineTo(0.00592, -0.002).lineTo(0.00592, -0.01).lineTo(0.00392, -0.01).close()
solid=wp_sketch0.add(loop0).extrude(0.004669924830615795)
