import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.125, 0.0).lineTo(0.125, 0.0).lineTo(0.105, -0.09798).lineTo(-0.105, -0.09798).lineTo(-0.125, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.7399208146390983)
