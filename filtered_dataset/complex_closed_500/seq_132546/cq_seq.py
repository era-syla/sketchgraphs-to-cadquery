import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02423, 0.2236).lineTo(-0.00123, 0.2236).lineTo(-0.00123, -0.0264).lineTo(-0.02423, -0.0264).lineTo(-0.02423, 0.2236).close()
solid=wp_sketch0.add(loop0).extrude(0.37272056783587604)
