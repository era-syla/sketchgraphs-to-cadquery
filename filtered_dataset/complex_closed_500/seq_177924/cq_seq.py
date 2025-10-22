import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0385, -0.0065).lineTo(-0.0455, -0.0065).lineTo(-0.0455, -0.0175).lineTo(-0.0385, -0.0175).lineTo(-0.0385, -0.0065).close()
solid=wp_sketch0.add(loop0).extrude(0.002444384549059468)
