import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.287, 0.2).lineTo(-0.01, 0.2).lineTo(-0.01, -0.01).lineTo(0.287, -0.01).lineTo(0.287, 0.2).close()
solid=wp_sketch0.add(loop0).extrude(0.8155927558233649)
