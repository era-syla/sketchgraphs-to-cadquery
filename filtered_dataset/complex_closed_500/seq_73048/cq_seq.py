import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.127, -0.11).lineTo(-0.107, -0.11).lineTo(-0.107, -0.08).lineTo(-0.127, -0.08).lineTo(-0.127, -0.11).close()
solid=wp_sketch0.add(loop0).extrude(0.0027864943958382416)
