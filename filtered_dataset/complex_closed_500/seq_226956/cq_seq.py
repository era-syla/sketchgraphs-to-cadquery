import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.012, 0.0).lineTo(0.062, 0.0).lineTo(0.062, -0.045).lineTo(0.012, -0.045).lineTo(0.012, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.13175271405885067)
