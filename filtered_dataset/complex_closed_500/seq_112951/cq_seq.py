import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.01033, 0.0).lineTo(0.01849, 0.0).lineTo(0.01849, -0.0061).lineTo(-0.01033, -0.0061).lineTo(-0.01033, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.014990528995737284)
