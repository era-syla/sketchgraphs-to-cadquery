import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0125, 0.0325).lineTo(0.0125, 0.0325).lineTo(0.0125, -0.0325).lineTo(-0.0125, -0.0325).lineTo(-0.0125, 0.0325).close()
solid=wp_sketch0.add(loop0).extrude(0.1037267391681087)
