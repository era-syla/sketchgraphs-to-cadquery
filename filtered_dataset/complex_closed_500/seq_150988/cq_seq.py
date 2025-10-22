import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.595, 0.2).lineTo(0.595, 0.2).lineTo(0.595, -0.055).lineTo(-0.595, -0.055).lineTo(-0.595, 0.2).close()
solid=wp_sketch0.add(loop0).extrude(0.6746223107200046)
