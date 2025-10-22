import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.517, 0.3475).lineTo(0.517, 0.3475).lineTo(0.517, -0.3475).lineTo(-0.517, -0.3475).lineTo(-0.517, 0.3475).close()
solid=wp_sketch0.add(loop0).extrude(1.060923568035006)
