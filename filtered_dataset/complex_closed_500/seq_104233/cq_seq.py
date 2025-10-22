import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-1.294, -5.0675).lineTo(-0.306, -5.0675).lineTo(-0.306, -4.8295).lineTo(-1.294, -4.8295).lineTo(-1.294, -5.0675).close()
solid=wp_sketch0.add(loop0).extrude(0.2882422292568486)
