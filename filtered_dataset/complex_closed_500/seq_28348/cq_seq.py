import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06452, -0.03428).lineTo(0.04867, -0.03428).lineTo(0.04867, 0.03752).lineTo(-0.06452, 0.03752).lineTo(-0.06452, -0.03428).close()
solid=wp_sketch0.add(loop0).extrude(0.03192379073968142)
