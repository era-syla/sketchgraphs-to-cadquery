import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.0075).lineTo(-0.0252, 0.0075).lineTo(-0.0252, -0.0105).lineTo(0.0, -0.0105).lineTo(0.0252, -0.0105).lineTo(0.0252, 0.0075).lineTo(-0.0, 0.0075).close()
solid=wp_sketch0.add(loop0).extrude(0.06296426859419323)
