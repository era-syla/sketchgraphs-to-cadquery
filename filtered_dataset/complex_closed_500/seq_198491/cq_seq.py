import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.17918, -0.23894).lineTo(-0.17642, -0.23894).lineTo(-0.17642, -0.22662).lineTo(0.17918, -0.22662).lineTo(0.17918, -0.23894).close()
solid=wp_sketch0.add(loop0).extrude(0.3141004713413018)
