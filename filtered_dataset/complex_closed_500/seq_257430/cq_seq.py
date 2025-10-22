import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.1016, 0.0635).lineTo(0.0762, 0.0635).lineTo(0.0762, 0.0381).lineTo(0.1016, 0.0381).lineTo(0.1016, 0.0635).close()
solid=wp_sketch0.add(loop0).extrude(0.0027590204656193114)
