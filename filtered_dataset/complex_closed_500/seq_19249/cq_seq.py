import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02373, -0.15523).lineTo(-0.02959, -0.15523).lineTo(-0.02959, 0.04796).lineTo(0.02373, 0.04796).lineTo(0.02373, -0.15523).close()
solid=wp_sketch0.add(loop0).extrude(-0.10712061289120317)
