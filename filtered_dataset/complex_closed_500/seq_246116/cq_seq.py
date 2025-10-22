import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.09362, -0.02102).lineTo(0.10836, -0.02102).lineTo(0.10836, -0.03093).lineTo(0.09362, -0.03093).lineTo(0.09362, -0.02102).close()
solid=wp_sketch0.add(loop0).extrude(0.030870742207789948)
