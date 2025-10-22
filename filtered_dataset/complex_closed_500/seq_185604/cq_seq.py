import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.17551, 1.1882).lineTo(-0.1778, 1.1882).lineTo(-0.17666, 1.18622).lineTo(-0.17551, 1.1882).close()
solid=wp_sketch0.add(loop0).extrude(0.005510504976313236)
