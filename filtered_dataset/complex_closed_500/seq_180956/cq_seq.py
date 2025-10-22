import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.06859, 0.04895).lineTo(0.04141, 0.04895).lineTo(0.04141, -0.02105).lineTo(-0.06859, -0.02105).lineTo(-0.06859, 0.04895).close()
solid=wp_sketch0.add(loop0).extrude(0.29037196672538906)
