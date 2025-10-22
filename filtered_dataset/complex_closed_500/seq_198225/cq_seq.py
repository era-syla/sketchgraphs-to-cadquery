import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.10116, 0.07438).lineTo(-0.10116, 0.07438).lineTo(-0.10116, -0.07438).lineTo(0.10116, -0.07438).lineTo(0.10116, 0.07438).close()
solid=wp_sketch0.add(loop0).extrude(0.5774570017662539)
