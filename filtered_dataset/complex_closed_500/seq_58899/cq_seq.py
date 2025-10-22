import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02932, 0.03063).lineTo(-0.04132, 0.03063).lineTo(-0.04132, 0.04263).lineTo(-0.02932, 0.04263).lineTo(-0.02932, 0.03063).close()
solid=wp_sketch0.add(loop0).extrude(0.0327256270982651)
