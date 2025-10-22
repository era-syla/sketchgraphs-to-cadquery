import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.003, -0.0125).lineTo(-0.003, 0.0125).lineTo(0.003, 0.0125).lineTo(0.003, -0.0125).lineTo(-0.003, -0.0125).close()
solid=wp_sketch0.add(loop0).extrude(0.018397062833824165)
