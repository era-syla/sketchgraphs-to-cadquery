import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0175, 0.0155).lineTo(0.0175, 0.0155).lineTo(0.0175, -0.0145).lineTo(-0.0175, -0.0145).lineTo(-0.0175, 0.0155).close()
solid=wp_sketch0.add(loop0).extrude(0.024273932485813877)
