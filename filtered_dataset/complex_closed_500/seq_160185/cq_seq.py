import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0125, 0.0112).lineTo(0.0125, 0.0112).lineTo(0.0125, 0.0032).lineTo(-0.0125, 0.0032).lineTo(-0.0125, 0.0112).close()
solid=wp_sketch0.add(loop0).extrude(-0.04970159808769407)
