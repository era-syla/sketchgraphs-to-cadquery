import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.4572, -1.3208).lineTo(-0.3683, -1.3208).lineTo(-0.3683, -1.3589).lineTo(-0.4572, -1.3589).lineTo(-0.4572, -1.3208).close()
solid=wp_sketch0.add(loop0).extrude(-0.05846454220752651)
