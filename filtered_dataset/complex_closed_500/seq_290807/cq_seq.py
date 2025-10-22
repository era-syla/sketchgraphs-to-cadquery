import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02, 0.0155).lineTo(-0.02, 0.0155).lineTo(-0.02, -0.0155).lineTo(0.02, -0.0155).lineTo(0.02, 0.0155).close()
solid=wp_sketch0.add(loop0).extrude(-0.06826017546561923)
