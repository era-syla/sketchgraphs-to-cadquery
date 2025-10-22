import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00246, 0.0083).lineTo(0.00254, 0.0083).lineTo(0.00254, 0.0063).lineTo(-0.00246, 0.0063).lineTo(-0.00246, 0.0083).close()
solid=wp_sketch0.add(loop0).extrude(0.010032127252875807)
