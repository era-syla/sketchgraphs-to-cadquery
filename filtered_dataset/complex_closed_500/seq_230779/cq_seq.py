import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02603, 0.03262).lineTo(-0.02603, 0.03262).lineTo(-0.02603, 0.05863).lineTo(0.02603, 0.05863).lineTo(0.02603, 0.03262).close()
solid=wp_sketch0.add(loop0).extrude(0.006894184726930186)
