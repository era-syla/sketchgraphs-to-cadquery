import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(-0.88502, 0.0).lineTo(-0.8483, 2.16).lineTo(-1.7483, 2.16).lineTo(-1.7483, 2.96).lineTo(0.07085, 2.96).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(6.547593754370474)
